""" Converts the certification documentation to a markdown format for a
site based on https://pages.18f.gov/guides-template/ """


from yaml import dump, load


def load_yaml(filename):
    """ Load a specific yaml file """
    with open(filename, 'r') as yaml_file:
        return load(yaml_file)


def yaml_writer(data, filename):
    """ Write data to a yaml file """
    with open(filename, 'w') as yaml_file:
        yaml_file.write(dump(data, default_flow_style=False))


def write_markdown(output_path, filename, text):
    """ Write text to a markdown file """
    file_name = output_path + '/pages/' + filename + '.md'
    with open(file_name, 'w') as f:
        f.write(text)


def create_standards_nav(standard_key):
    """ Creates a dictionary for a main page following the config file format
    For more info about the _config.yml file visit :
    https://pages.18f.gov/guides-template/update-the-config-file/ """
    return {
        'text': standard_key + " Documentation",
        'url': standard_key + '/',
        'internal': True,
        'children': list()
    }


def create_control_nav(control_key, control):
    """ Creates a dictionary for a child page following the config file format
    For more info about the _config.yml file visit :
    https://pages.18f.gov/guides-template/update-the-config-file/ """
    return {
        'text': control_key + " " + control['meta']['name'],
        'url': control_key + '/',
        'internal': True,
    }


def update_config(config_folder, navigation):
    """ Loads and modifies the `navigation` data for the _config.yml file
    For more info about the _config.yml file visit :
    https://pages.18f.gov/guides-template/update-the-config-file/ """
    config_filename = config_folder + "/_config.yml"
    config_data = load_yaml(config_filename)
    config_data['navigation'] = [{
        'text': 'Introduction',
        'url': 'index.html',
        'internal': True,
    }]
    config_data['navigation'].extend(navigation)
    yaml_writer(data=config_data, filename=config_filename)


def create_front_matter(standard_key, control_key, control):
    """ Generate yaml front matter for pages text
    For more info about pages front matter visit -
    https://pages.18f.gov/guides-template/add-a-new-page/ """
    text = '---\npermalink: /{0}/{1}/\n'.format(standard_key, control_key)
    text += 'title: {0} - {1}\n'.format(control_key, control['meta']['name'])
    text += 'parent: {0} Documentation\n---\n'.format(standard_key)
    return text


def convert_references(references):
    """ Converts references data to markdown url bullet point. """
    text = ''
    for reference in references:
        text += '\n* [{0}]({1})\n'.format(
            reference['reference_name'], reference['reference_url'])
    return text


def covert_governors(governors):
    """ Converts governors data to markdown url bullet point. """
    text = ''
    for reference in governors:
        text += '\n* [{0}]({1})\n'.format(
            reference['governor_name'], reference['governor_url'])
    return text


def create_content(control):
    """ Generate the markdown text from each `justification` """
    text = ''
    for justification in control.get('justifications', []):
        text += '\n## {0}\n'.format(justification.get('name'))
        text += justification.get('narative')
        references = justification.get('references')
        if references:
            text += '\n### References\n'
            text += convert_references(references)
        governors = justification.get('governors')
        if governors:
            text += '\n### Governors\n'
            text += covert_governors(governors)
        text += "\n--------\n"
    return text


def create_markdown(output_path, standard_key, control_key=None, control=None):
    """ Generate the markdown file from each standards and control """
    if control_key and control:
        text = create_front_matter(standard_key, control_key, control)
        text += create_content(control)
        filename = control_key
    else:
        text = '---\npermalink: /{0}/\n'.format(standard_key)
        text += 'title: {0} Documentation\n---\n'.format(standard_key)
        filename = standard_key
    write_markdown(output_path, filename, text)


def convert_certifications(certification_path, output_path):
    """ Convert certification to pages format """
    navigation_config = []
    certification = load_yaml(certification_path)
    for standard_key in certification['standards']:
        standard_navigation = create_standards_nav(standard_key)
        for control_key in certification['standards'][standard_key]:
            control = certification['standards'][standard_key][control_key]
            standard_navigation['children'].append(
                create_control_nav(control_key, control)
            )
            create_markdown(output_path, standard_key, control_key, control)
        navigation_config.append(standard_navigation)
        create_markdown(output_path, standard_key)
    update_config(output_path, navigation_config)


if __name__ == "__main__":
    convert_certifications(
        certification_path="exports/certifications/FISMA.yaml",
        output_path="exports/Pages"
    )

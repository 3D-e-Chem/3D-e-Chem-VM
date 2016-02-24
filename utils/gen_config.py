#!/usr/bin/env python

import argparse

import github3
import yaml

parser = argparse.ArgumentParser(description='Generate Github variable for jekyll')
parser.add_argument('organization', help='Github organization or user name')
parser.add_argument('repository', help='Github repository name')
parser.add_argument('configfn',
                    default='_config.yml',
                    type=argparse.FileType('w'),
                    help="Filename for config file. Default _config.yml. Use - for stdout")
args = parser.parse_args()

gh = github3.GitHub()

repo = gh.repository(args.organization, args.repository)

config = {
    'title': repo.name,
    'description': repo.description,
    'baseurl': '/' + repo.name,
    'project_name': repo.owner.login,
    'urls': {
        'changelog': repo.html_url + '/blob/master/CHANGELOG.md',
        'download': repo.html_url + '/releases/latest',
        'issues': repo.html_url + '/issues',
        'repo': repo.html_url,
        'project': '<FIXME>',
        'docs': repo.html_url + '/wiki',
    },
    'languages': [l[0] for l in repo.languages()],
    'license': repo.license().license['name'],
    'partners': [{
        'logo_url': 'https://www.esciencecenter.nl/img/pressroom/ESCIENCE_logo_C_nl_cyanblack.jpg',
        'url': 'https://www.esciencecenter.nl'
    }, {
        'logo_url': '<FIXME AND OPTIONALLY REPEATME>',
        'url': '<FIXME AND OPTIONALLY REPEATME>'
    }],
    'markdown': 'kramdown',
    'excludes': [
        'README.md',
        'utils',
    ],
    'keep_files': [
        'assets'
    ]
}

yaml.dump(config, args.configfn, default_flow_style=False)

# Contributing

We love pull requests from everyone. By participating in this project, you
agree to abide by the [code of conduct](CODE_OF_CONDUCT.md).

Fork, then clone the repo:

    git clone git@github.com:your-username/3D-e-Chem-VM.git

Set up your machine:

    pip install ansible

Make sure the tests pass:

    ansible-playbook -i localhost, --syntax-check playbook.yml

Make your change. Add tests for your change. Make the tests pass:

    ansible-playbook -i localhost, --syntax-check playbook.yml

Push to your fork and [submit a pull request](https://github.com/3D-e-Chem/3D-e-Chem-VM/compare/).

At this point you're waiting on us. We like to at least comment on pull requests
within three business days (and, typically, one business day). We may suggest
some changes or improvements or alternatives.

Some things that will increase the chance that your pull request is accepted:

* Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

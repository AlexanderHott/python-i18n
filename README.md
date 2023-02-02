# python-i18n

Python internationalization.

[Python `gettext` docs.](https://docs.python.org/3/library/gettext.html)

## Quick Start

1. Create a `locale` directory to store your translation files.

1. Create a translation template file (.pot) that contains all the text to translate.

    ```pot
    #: translate.py:8
    msgid "hello world"
    msgstr ""
    ```

1. Create a translation file (.po).

    ```bash
    $ cp locale/template.pot en-US.po
    ```

1. Fill out the translation file.

    ```po
    #: translate.py:8
    msgid "hello world"
    msgstr "Different Message"
    ```

1. Generate the binary translation file with `msgfmt`.

    ```bash
    $ msgfmt locale/en-US.po -o locale/en-US.mo
    ```

1. Repeat for all desired languages.

1. Create and use a translator.

    ```python
    import gettext

    localedir = './locale/'
    translator = gettext.GNUTranslations(open(localedir + "en-US.mo", "rb"))

    _ = translator.gettext
    print(_("hello world"))  # Different Message
    ```

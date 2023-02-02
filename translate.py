import gettext

localedir = './locale/'

translator = gettext.GNUTranslations(open(localedir + "en-US.mo", "rb"))
_ = translator.gettext
print(_("hello world"))


de_translator = gettext.GNUTranslations(open(localedir + "de.mo", "rb"))
_ = de_translator.gettext
print(_("hello world"))

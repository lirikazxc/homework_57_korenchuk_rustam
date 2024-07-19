from django.core.exceptions import ValidationError


def val_sum_len(value):
    if len(value) < 3:
        raise ValidationError('Описание должно быть длинее 3х символов')


def val_bad_words(value):
    bad_words = ['дурак', "stupid"]
    for word in bad_words:
        if word in value:
            raise ValidationError('Описание не должно содержать плохих слов!')

from django.conf import settings

def _validate_hospital_meta_data(**kwargs):
    hospital_data = {}
    for k, v in kwargs.items():
        assert isinstance(v, str), 'Each of the hospital settings must be of type str. You have given {} of {}'.format(v, type(v))
        if v.strip():
            hospital_data[k] = v
        else:
            hospital_data[k] = 'SET THE {}'.format(k).upper()
    return hospital_data


def hospital(request):
    '''
    Adds a hospital's cleaned meta data such as name, motto etc to the context of all views..
    '''
    kwargs = {
        'hospital_name': getattr(settings, 'HOSPITAL_NAME', ''),
        'hospital_slogan': getattr(settings, 'HOSPITAL_SLOGAN', ''),
    }

    clean_data = _validate_hospital_meta_data(**kwargs)

    return clean_data

from django import forms
from .parse import parse

setup = parse()


class ConfigForm(forms.Form):
    grid = forms.ChoiceField(choices=[('box', 'Box'), ('none', 'None')])
    chemistry_time_step = forms.FloatField(initial=setup['box model options']["chemistry time step [min]"])
    output_time_step = forms.FloatField(initial=setup['box model options']["output time step [hr]"])
    simulation_length = forms.FloatField(initial=setup['box model options']["output time step [hr]"])
    NO2_initial = forms.FloatField(initial=setup['chemical species']["NO2"]["initial value [mol m-3]"])
    NO_initial = forms.FloatField(initial=setup['chemical species']["NO"]["initial value [mol m-3]"])
    O3_initial = forms.FloatField(initial=setup['chemical species']["O3"]["initial value [mol m-3]"])
    ISOP_initial = forms.FloatField(initial=setup['chemical species']["ISOP"]["initial value [mol m-3]"])
    temperature = forms.FloatField(initial=setup['enviornmental conditions']["temperature"]["initial value [K]"])
    pressure = forms.FloatField(initial=setup['enviornmental conditions']["pressure"]["initial value [atm]"])


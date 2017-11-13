from flask import Blueprint, jsonify, request

from skynet.roku.models import RokuModel
from skynet.roku.forms import RokuKeypressForm, RokuLaunchForm

roku = Blueprint('roku', __name__, url_prefix='/roku')


@roku.route('/keypress')
def keypress():
    form_data = RokuKeypressForm(request.args)

    if not form_data.validate():
        return 'Invalid GET Args', 403

    roku_model = RokuModel()
    roku_model.load(
        'keypress',
        form_data.key.data
    )
    return jsonify(roku_model.send_command())

@roku.route('/launch')
def launch():
    form_data = RokuLaunchForm(request.args)

    if not form_data.validate():
        return 'Invalid GET Args', 403

    roku_model = RokuModel()
    roku_model.load(
        'launch',
        form_data.app_id.data
    )
    return jsonify(roku_model.send_command())
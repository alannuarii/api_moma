from app import app
from flask import jsonify, request
from app.controller.irradiance import Irradiance
from app.controller.weather import Weather
from app.controller.rom import ROM
from app.controller.user import User
from app.controller.prediction import (
    prediction,
    get_arr_irradiance,
    get_month_prediction,
)
from app.controller.rekap import (
    post_mode_operasi,
    post_max_irradiance,
    mode_correction,
)


@app.route("/login", methods=["GET", "POST"])
def login():
    object_user = User()
    if request.method == "POST":
        try:
            result = object_user.login()
            return jsonify(result), 200

        except Exception as e:
            error_message = {"message": "Terjadi kesalahan", "error": str(e)}
            return jsonify(error_message), 500

    response = {"message": "Metode HTTP yang diperlukan: POST"}
    return jsonify(response), 405


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            object_user = User()
            result = object_user.register()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim", "result": result}
    return jsonify(response), 200


@app.route("/irradiance", methods=["GET", "POST"])
def upload_irradiance():
    if request.method == "POST":
        try:
            object_irradiance = Irradiance()
            object_irradiance.upload_file()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim"}
    return jsonify(response), 200


@app.route("/irradiance/<tanggal>")
def get_irradiance(tanggal):
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_irradiance(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/irradiance-array/<tanggal>")
def get_array_irradiance(tanggal):
    try:
        data = get_arr_irradiance(tanggal)

        response = {"message": "Sukses", "data": data}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/last-irradiance")
def get_last_data_irradiance():
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_last_irradiance()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/irradiance/tanggal")
def get_irradiance_4days():
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_4days()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/irradiance/rekap/<month>")
def get_irradiance_month(month):
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_month_max_irradiance(month)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/weather-today")
def get_weather_today():
    try:
        object_weather = Weather()
        data_weather = object_weather.get_data_weather(0)
        weather = data_weather["weather"]
        temperature = data_weather["t"]
        humidity = data_weather["hu"]
        wind = data_weather["ws"]

        response = {
            "message": "Sukses",
            "data": {
                "weather": weather,
                "temperature": temperature,
                "humidity": humidity,
                "wind": wind,
            },
        }
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/weather-tomorrow")
def get_weather_tomorrow():
    try:
        object_weather = Weather()
        data_weather = object_weather.get_data_weather(24)
        weather = data_weather["weather"]
        temperature = data_weather["t"]
        humidity = data_weather["hu"]
        wind = data_weather["ws"]

        response = {
            "message": "Sukses",
            "data": {
                "weather": weather,
                "temperature": temperature,
                "humidity": humidity,
                "wind": wind,
            },
        }

        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/weather/rekap/<month>")
def get_weather_month(month):
    try:
        object_weather = Weather()
        result = object_weather.get_weather_month(month)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rom", methods=["GET", "POST"])
def upload_rom():
    if request.method == "POST":
        try:
            object_rom = ROM()
            object_rom.upload_rom()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim"}
    return jsonify(response), 200


@app.route("/rompltd/<tanggal>")
def get_rompltd(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_pltd(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompltd/week")
def get_rompltd_week():
    try:
        object_rom = ROM()
        result = object_rom.get_pltd_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompv/<tanggal>")
def get_rompv(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_pv(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompv/week")
def get_rompv_week():
    try:
        object_rom = ROM()
        result = object_rom.get_pv_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rombss/<tanggal>")
def get_rombss(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_bss(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rombss/week")
def get_rombss_week():
    try:
        object_rom = ROM()
        result = object_rom.get_bss_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompltd/rekap/<month>")
def get_rompltd_month(month):
    try:
        object_rom = ROM()
        result = object_rom.get_data_month(month, "rompltd")
        unit6 = []
        unit7 = []

        for item in result:
            unit = item["unit"]
            if item["status"] == 1:
                item["status"] = "Stand by"
            elif item["status"] == 0:
                item["status"] = "Pemeliharaan"

            if unit == 6:
                unit6.append(item)
            elif unit == 7:
                unit7.append(item)

        response = {"message": "Sukses", "data": [unit6, unit7]}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompv/rekap/<month>")
def get_rompv_month(month):
    try:
        object_rom = ROM()
        result = object_rom.get_data_month(month, "rompv")
        unit1 = []
        unit2 = []

        for item in result:
            unit = item["unit"]
            if item["status"] == 1:
                item["status"] = "Stand by"
            elif item["status"] == 0:
                item["status"] = "Pemeliharaan"

            if unit == 1:
                unit1.append(item)
            elif unit == 2:
                unit2.append(item)

        response = {"message": "Sukses", "data": [unit1, unit2]}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rombss/rekap/<month>")
def get_rombss_month(month):
    try:
        object_rom = ROM()
        result = object_rom.get_data_month(month, "rombss")
        unit1 = []
        unit2 = []

        for item in result:
            unit = item["unit"]
            if item["status"] == 1:
                item["status"] = "Stand by"
            elif item["status"] == 0:
                item["status"] = "Pemeliharaan"

            if unit == 1:
                unit1.append(item)
            elif unit == 2:
                unit2.append(item)

        response = {"message": "Sukses", "data": [unit1, unit2]}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/forcast-today/<tanggal>")
def get_forcast_today(tanggal):
    try:
        today = prediction(tanggal, 0)

        response = {"message": "Sukses", "data": today}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/forcast-tomorrow/<tanggal>")
def get_forcast_tomorrow(tanggal):
    try:
        tomorrow = prediction(tanggal, 24)

        response = {"message": "Sukses", "data": tomorrow}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/mode/rekap/<month>")
def get_mode_month(month):
    try:
        result = get_month_prediction(month)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/sync", methods=["GET", "POST"])
def synchrone_data():
    if request.method == "POST":
        try:
            post_max_irradiance()
            post_mode_operasi()

        except Exception as e:
            error_response = {"message": "Gagal synchrone data", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Synchrone data berhasil"}
    return jsonify(response), 200


@app.route("/correction", methods=["GET", "POST"])
def correction():
    if request.method == "POST":
        try:
            mode_correction()

        except Exception as e:
            error_response = {"message": "Data tidak ditemukan", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Koreksi data berhasil"}
    return jsonify(response), 200


@app.route('/autoschedule', methods=['POST'])
def auto_schedule():
    try:
        object_irradiance = Irradiance()
        object_weather = Weather()
        object_rom = ROM()
        object_irradiance.auto_input_irradiance()
        object_rom.auto_upload_rom('rompltd')
        object_rom.auto_upload_rom('rompv')
        object_rom.auto_upload_rom('rombss')
        object_weather.insert_weather()
        post_max_irradiance()
        post_mode_operasi()
        mode_correction()
    
        response = {"message": "Data berhasil dikirim"}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Data gagal terkirim", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/manualirradiance/<tanggal>")
def manual_irradiance(tanggal):
    try:
        obj_irr = Irradiance()
        obj_irr.manual_input_irradiance(tanggal)
        response = {"message": "Sukses"}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Data tidak ditemukan", "error": str(e)}
        return jsonify(error_response), 500



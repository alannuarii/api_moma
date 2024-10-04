import requests
from db import connection
from datetime import datetime, timedelta


class Weather:
    def get_data_weather(delta):
        # URL API BMKG yang akan diakses
        url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=71.03.17.1016"

        # Membuat permintaan GET ke API
        response = requests.get(url)

        # Memeriksa status response
        if response.status_code == 200:
            # Mengubah response menjadi format JSON
            data = response.json()
            
            weather = data["data"]
            # Tentukan tanggal hari ini tetapi tetap pada jam 11:00:00
            now = datetime.now()
            today = datetime(now.year, now.month, now.day, 11, 0, 0)  # Contoh: 2024-10-04 11:00:00
            time_data = today + timedelta(hours=delta)

            # Filter data cuaca berdasarkan local_datetime yang sesuai dengan hari ini pada jam 11:00:00
            list_result = []

            for lokasi_data in weather:
                for periode in lokasi_data["cuaca"]:
                    for cuaca in periode:
                        # Konversi string local_datetime ke datetime object
                        local_dt = datetime.strptime(cuaca["local_datetime"], "%Y-%m-%d %H:%M:%S")
                        
                        # Cek apakah local_datetime sama dengan hari ini (tanggal saat ini pada jam 11:00:00)
                        if local_dt == time_data:
                            list_result.append(cuaca)

            return list_result[0]
        else:
            print(f"Error: Tidak dapat mengakses API BMKG. Status code: {response.status_code}")

    # def get_weather(self, hour):
    #     cuaca = self.sangihe.find(id="501536").find(id="weather")
    #     h12 = cuaca.find(h=hour).value.string
    #     result = h12
    #     return result

    # def get_temperature(self, hour):
    #     temperature = self.sangihe.find(id="501536").find(id="t")
    #     h12 = temperature.find(h=hour).value.string
    #     result = h12
    #     return result

    # def get_humidity(self, hour):
    #     humidity = self.sangihe.find(id="501536").find(id="hu")
    #     h12 = humidity.find(h=hour).value.string
    #     result = h12
    #     return result

    # def get_wind(self, hour):
    #     humidity = self.sangihe.find(id="501536").find(id="ws")
    #     h12 = humidity.find(h=hour).value.string
    #     result = h12
    #     return result

    def insert_weather(self):
        tanggal = datetime.today().strftime("%Y-%m-%d")
        if self.get_kode_weather(tanggal):
            if self.get_kode_weather(tanggal)[0]['kode'] != int(self.get_data_weather(0)["weather"]):
                self.update_kode_weather(tanggal)
            else:
                pass
        else:
            kode = int(self.get_data_weather(0)["weather"])
            query = f"INSERT INTO weather (tanggal, kode) VALUES (%s, %s)"
            value = [tanggal, kode]
            connection(query, "insert", value)


    def get_kode_weather(self, tanggal):
        query = f"SELECT kode FROM weather WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, 'select', value)
        return result
    
    def get_weather_month(self, bulan):
        query = f"SELECT tanggal, kode FROM weather WHERE DATE_FORMAT(tanggal, '%Y-%m') = %s"
        value = [bulan]
        result = connection(query, 'select', value)
        return result
    
    def update_kode_weather(self, tanggal):
        query = f"UPDATE weather SET kode = %s WHERE tanggal = %s"
        value = [self.get_weather('12'), tanggal]
        connection(query, 'update', value)

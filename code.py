import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def submit_form_data(data):
    try:
        # กำหนด scope สำหรับ Google Sheets API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        # โหลด credentials จากไฟล์ JSON
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

        # เชื่อมต่อกับ Google Sheets API
        client = gspread.authorize(creds)

        # เปิดสเปรดชีตและชีต
        sheet = client.open_by_key('1V5W5JJMuPQyy6pqerd7saHh89HAeXUH6Tpfh52dpsQo').sheet1  # หรือใช้ sheet.worksheet('Sheet1')

        # เพิ่มข้อมูลเป็นแถวใหม่
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
            data['name'],
            data['department'],
            data['phone'],
            data['date1'],
            data['date2'],
            data['count'],
            data['room']
        ]
        sheet.append_row(row)

        return {'status': 'success', 'message': 'บันทึกข้อมูลสำเร็จ!'}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# ตัวอย่างการใช้งาน
data = {
    'name': 'John Doe',
    'department': 'IT',
    'phone': '0812345678',
    'date1': '2023-10-26',
    'date2': '2023-10-27',
    'count': '10',
    'room': 'พัก'
}

result = submit_form_data(data)
print(result)
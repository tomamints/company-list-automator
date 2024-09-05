import requests
from bs4 import BeautifulSoup
import csv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def scrape_companies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    companies = []
    
    # ここでHTMLの構造に基づいて企業データを抽出
    # 例: company_elements = soup.find_all('div', class_='company-item')
    # for element in company_elements:
    #     name = element.find('h2').text
    #     # その他の必要な情報を抽出
    #     companies.append({'name': name, ...})
    
    return companies

def save_to_csv(companies, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=companies[0].keys())
        writer.writeheader()
        writer.writerows(companies)

def upload_to_sheets(filename):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {'title': 'New Companies List'}
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet).execute()
        sheet_id = spreadsheet.get('spreadsheetId')
        
        with open(filename, 'r', encoding='utf-8') as file:
            csv_content = file.read()
        
        body = {
            'requests': [{
                'pasteData': {
                    'coordinate': {
                        'sheetId': 0,
                        'rowIndex': 0,
                        'columnIndex': 0,
                    },
                    'data': csv_content,
                    'type': 'PASTE_NORMAL',
                    'delimiter': ',',
                }
            }]
        }
        
        service.spreadsheets().batchUpdate(
            spreadsheetId=sheet_id, body=body).execute()
        print(f'Spreadsheet created: https://docs.google.com/spreadsheets/d/{sheet_id}')
    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    url = 'https://kaishalist.com/?prefecture=23'
    companies = scrape_companies(url)
    csv_filename = 'new_companies.csv'
    save_to_csv(companies, csv_filename)
    upload_to_sheets(csv_filename)
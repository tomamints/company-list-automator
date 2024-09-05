# 企業リスト自動化プロジェクト

このプロジェクトは、指定されたウェブサイトから新規企業の情報を自動的にスクレイピングし、Google Sheetsに保存するためのものです。

## 実行手順

1. 環境設定
   - Python 3.7以上がインストールされていることを確認してください。
   - 使用しているPythonのバージョンを確認します：
     ```
     python3 --version
     ```
   - 必要なPythonライブラリをインストールします：
     ```
     python3 -m pip install requests beautifulsoup4 google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```
   - インストールされたライブラリを確認します：
     ```
     python3 -m pip list
     ```

2. Google Cloud Projectの設定
   - [Google Cloud Console](https://console.cloud.google.com/)にアクセスし、新しいプロジェクトを作成します。
   - Google Sheets APIを有効にします。
   - 認証情報を作成し、JSONキーファイルをダウンロードします。
   - ダウンロードしたJSONファイルを`token.json`という名前でプロジェクトのルートディレクトリに配置します。

3. スクリプトの設定
   - `src/scripts/scrape_companies.py`ファイルを開きます。
   - `url`変数を、スクレイピングしたいウェブページのURLに更新します。

4. スクリプトの実行
   - コマンドラインで以下のコマンドを実行します：
     ```
     python3 src/scripts/scrape_companies.py
     ```

5. 結果の確認
   - スクリプトが正常に実行されると、新しいGoogle Sheetsのスプレッドシートが作成されます。
   - コンソールに表示されるURLをクリックして、作成されたスプレッドシートを確認します。

## トラブルシューティング

- `ModuleNotFoundError: No module named 'requests'`のようなエラーが発生した場合：
  - 使用しているPython環境が正しいか確認してください。
  - 以下のコマンドを実行して、Pythonの実行パスを確認します：
    ```
    which python3
    ```
  - 必要なライブラリが正しくインストールされているか確認します：
    ```
    python3 -m pip list
    ```
  - 上記の確認後も問題が解決しない場合は、以下のコマンドを実行して、必要なライブラリを個別にインストールしてください：
    ```
    python3 -m pip install requests
    python3 -m pip install beautifulsoup4
    python3 -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

## 注意事項

- ウェブサイトの利用規約を確認し、スクレイピングが許可されていることを確認してください。
- 大量のリクエストを短時間で送信しないよう、適切な間隔を設けてスクリプトを実行してください。
- エラーが発生した場合は、エラーメッセージを確認し、必要に応じてスクリプトを調整してください。

## 定期実行の設定（オプション）

スクリプトを定期的に実行したい場合は、以下のいずれかの方法を検討してください：

1. cron（Unix系システム）やTask Scheduler（Windows）を使用して、定期的にスクリプトを実行するようスケジュールを設定する。
2. クラウドサービス（例：Google Cloud Functions + Cloud Scheduler）を利用して、定期的にスクリプトを実行する。

これらの設定方法については、それぞれのシステムやサービスのドキュメントを参照してください。
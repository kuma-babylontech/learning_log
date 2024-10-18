# 最短距離でゼロからしっかり学ぶ Python 入門　実践編

第 7 章「Django をはじめる」で作成する、「学習ノート」Web アプリケーション

## 機能

- ユーザー認証（サインアップ、ログイン、ログアウト）
- トピックの作成、読み取り、更新、削除
- 各トピックのエントリーの作成、読み取り、更新、削除

## インストール

1. リポジトリをクローンします:
   ```bash
   git clone https://github.com/yourusername/learning_log.git
   ```
2. プロジェクトディレクトリに移動します:
   ```bash
   cd learning_log
   ```
3. 仮想環境を作成します:
   ```bash
   python -m venv ll_env
   ```
4. 仮想環境を有効化します:
   - Windows の場合:
     ```bash
     ll_env\Scripts\activate
     ```
   - macOS および Linux の場合:
     ```bash
     source ll_env/bin/activate
     ```
5. 必要なパッケージをインストールします:
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 開発サーバーを実行します:
   ```bash
   python manage.py runserver
   ```
2. ウェブブラウザを開き、`http://127.0.0.1:8000`にアクセスします。

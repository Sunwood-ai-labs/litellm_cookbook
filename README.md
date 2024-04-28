
<p align="center">
<img src="docs/litellm_cookbook_icon.jpeg" width="100%">
<br>
<!-- <h1 align="center">Litellm Cookbook</h1> -->
<h2 align="center">
  ～ Cook up AI with ease ～

[![litellm_cookbook - Sunwood-ai-labs](https://img.shields.io/static/v1?label=litellm_cookbook&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/litellm_cookbook/Sunwood-ai-labs "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/litellm_cookbook/Sunwood-ai-labs?style=social)](https://github.com/litellm_cookbook/Sunwood-ai-labs)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/litellm_cookbook/Sunwood-ai-labs?style=social)](https://github.com/litellm_cookbook/Sunwood-ai-labs)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/litellm_cookbook)](https://github.com/Sunwood-ai-labs/litellm_cookbook)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/litellm_cookbook)](https://github.com/Sunwood-ai-labs/litellm_cookbook)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/litellm_cookbook?sort=date&color=red)](https://github.com/Sunwood-ai-labs/litellm_cookbook)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/litellm_cookbook?color=orange)](https://github.com/Sunwood-ai-labs/litellm_cookbook)

  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。


litellm_cookbookは、最新の自然言語処理技術を手軽に体験できるリポジトリです。litellmとollamaを組み合わせることで、高性能な言語モデルを簡単に利用できます。

## 特徴

- 🚀 最先端の言語モデルを使用
- 📦 Dockerを使用した簡単な環境構築

## 環境構築

1. litellm_cookbook用のConda環境を作成します。

   ```bash
   conda create -n litellm_cookbook python=3.11
   ```

2. 作成したConda環境をアクティベートします。

   ```bash
   conda activate litellm_cookbook
   ```

3. litellmをインストールします。

   ```bash
   pip install litellm
   ```

4. ollamaコンテナを起動し、言語モデルを実行します。

   ```bash
   docker-compose up 
   docker compose exec -it ollama ollama run llama3
   docker compose exec -it ollama ollama run llama2
   docker compose exec -it ollama ollama run gemma
   ```

5. 利用可能な言語モデルを確認します。

   ```bash
   docker compose exec -it ollama ollama ls
   ```

    ```bash
    NAME            ID              SIZE    MODIFIED
    gemma:latest    a72c7f4d0a15    5.0 GB  8 minutes ago
    llama3:latest   a6990ed6be41    4.7 GB  8 minutes ago
    ```

## クックブック

`cookbook/example.01.py`は、litellmを使用して言語モデルにクエリを送信する例です。このスクリプトでは、llama3とgemmaモデルに対して、「20語で答えてください。あなたは誰ですか？」というクエリを送信し、その応答を表示します。

### 出力例
```bash
Choices(finish_reason='stop', index=0, message=Message(content="Nice to meet you! 😊 I am LLaMA, a large language model trained by a team of researcher at Meta AI. My primary function is to generate human-like text responses to user input, and I'm constantly learning and improving my abilities based on the conversations I have with users like you. I may not be perfect, but I'll do my best to provide helpful and accurate information in our 20-language conversation! 🤖", role='assistant'))
--------------------
Choices(finish_reason='stop', index=0, message=Message(content='私の詳細な情報は教えておりません。必要に応じて、必要な情報を提供します。', role='assistant'))
```

## litellm設定

`litellm/config.yaml`は、litellmの設定ファイルです。このファイルでは、使用する言語モデルとそのパラメータを指定します。また、litellmの動作に関する一般的な設定も含まれています。

## 使用方法

1. `activate-litellm_cookbook.bat`を実行して、litellm_cookbook用のConda環境をアクティベートします。

2. `cookbook`ディレクトリ内のPythonスクリプトを実行して、言語モデルの実験を行います。

このリポジトリを使用することで、litellmとollamaを組み合わせた言語モデルの実験を簡単に行うことができます。
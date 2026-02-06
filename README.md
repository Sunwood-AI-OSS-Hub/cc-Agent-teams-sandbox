# cc-Agent-teams-sandbox

<div align="center">
  <img src="assets/release-header-v0.1.0.svg" alt="Agent Teams Sandbox Release Header" width="600">
</div>

Claude Codeのエージェントチーム機能を試すためのサンドボックスリポジトリ。

## 概要

このリポジトリは、Claude CodeのAgent Teams機能の検証と実験のために作成されました。テーマに沿ったエージェントチームを結成し、協調してタスクを達成する様子を観察・実験します。

## 特徴

- 🐱 **テーマ別エージェントチーム**: 桃太郎、魔王軍団、猫のシステム会社など、様々なテーマでチームを結成
- 🤖 **自動リリースシステム**: GitHub Actionsで猫テーマのヘッダー画像付きリリースノートを自動生成
- 🎨 **カスタムSVGヘッダー**: `.github/scripts/generate-header.py` でアニメーション付きのヘッダー画像を生成

## 自動リリースシステム

リリースを作成すると、自動的に以下の処理が実行されます：

1. 猫テーマのSVGヘッダー画像生成
2. Gitコミット履歴からチェンジログ作成
3. リリースノートの自動更新

### 生成されるヘッダー画像

- 浮遊する猫の顔（アニメーション付き）
- 揺れるしっぽ
- キラキラ光るスター
- 猫の肉球パターン背景
- バージョンバッジ

## エージェントチームの例

### Nyan Corporation 🐱

猫の運営するシステム会社をテーマにしたエージェントチーム。

| メンバー | 役割 |
|----------|------|
| Boss Cat | 代表取締役猫・チーム統括 |
| Repository Cat | リポジトリ整備担当 |
| Release Cat | リリース担当 |
| QA Cat | テスト・検証担当 |

## リリース

- [v0.1.0](https://github.com/Sunwood-AI-OSS-Hub/cc-Agent-teams-sandbox/releases/tag/v0.1.0) - Initial Release

## ライセンス

MIT

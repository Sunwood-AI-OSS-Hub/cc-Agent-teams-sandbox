#!/usr/bin/env python3
"""
GitHubリリースノート用のヘッダー画像を生成するスクリプト

Pillowを使用して、猫のシステム会社「Nyan Corporation」の
リリースノート用ヘッダー画像を生成します。
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow is not installed.", file=sys.stderr)
    print("Install with: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def create_header_image(
    version: str,
    output_path: str,
    width: int = 1200,
    height: int = 400,
    theme: str = "default"
) -> None:
    """
    リリースノート用ヘッダー画像を生成します

    Args:
        version: リリースバージョン（例: v1.0.0）
        output_path: 出力ファイルパス
        width: 画像の幅（デフォルト: 1200）
        height: 画像の高さ（デフォルト: 400）
        theme: テーマ（default/dark/light）
    """

    # テーマに応じた色設定
    themes = {
        "default": {
            "bg_start": (40, 40, 60),
            "bg_end": (20, 20, 40),
            "accent": (100, 180, 255),
            "text": (255, 255, 255),
            "subtext": (200, 200, 220)
        },
        "dark": {
            "bg_start": (30, 30, 30),
            "bg_end": (10, 10, 10),
            "accent": (255, 200, 100),
            "text": (255, 255, 255),
            "subtext": (180, 180, 180)
        },
        "light": {
            "bg_start": (240, 240, 250),
            "bg_end": (220, 220, 240),
            "accent": (100, 100, 180),
            "text": (40, 40, 60),
            "subtext": (100, 100, 120)
        }
    }

    colors = themes.get(theme, themes["default"])

    # 画像を作成
    img = Image.new("RGB", (width, height), colors["bg_start"])
    draw = ImageDraw.Draw(img)

    # グラデーション背景
    for y in range(height):
        ratio = y / height
        r = int(colors["bg_start"][0] * (1 - ratio) + colors["bg_end"][0] * ratio)
        g = int(colors["bg_start"][1] * (1 - ratio) + colors["bg_end"][1] * ratio)
        b = int(colors["bg_start"][2] * (1 - ratio) + colors["bg_end"][2] * ratio)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

    # アクセントライン
    line_height = 8
    for i in range(line_height):
        alpha = int(255 * (1 - i / line_height))
        draw.rectangle(
            [(0, i), (width, i + 1)],
            fill=colors["accent"]
        )

    # デコレーション（猫の顔のようなパターン）
    # 左耳
    draw.polygon([
        (80, 80), (120, 40), (160, 80)
    ], fill=colors["accent"])
    # 右耳
    draw.polygon([
        (width - 160, 80), (width - 120, 40), (width - 80, 80)
    ], fill=colors["accent"])

    # フォントの設定
    try:
        # システムフォントを使用
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        version_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
        company_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except (OSError, IOError):
        # フォントが見つからない場合はデフォルトを使用
        title_font = ImageFont.load_default()
        version_font = ImageFont.load_default()
        company_font = ImageFont.load_default()

    # テキストを描画
    # 会社名
    company_text = "Nyan Corporation"
    company_bbox = draw.textbbox((0, 0), company_text, font=company_font)
    company_width = company_bbox[2] - company_bbox[0]
    draw.text(
        ((width - company_width) // 2, 120),
        company_text,
        fill=colors["text"],
        font=company_font
    )

    # バージョン
    version_text = f"Release {version}"
    version_bbox = draw.textbbox((0, 0), version_text, font=version_font)
    version_width = version_bbox[2] - version_bbox[0]
    draw.text(
        ((width - version_width) // 2, 200),
        version_text,
        fill=colors["accent"],
        font=version_font
    )

    # サブテキスト
    subtitle = "にゃあ〜、新しいバージョンが登場したにゃ！"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=company_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(
        ((width - subtitle_width) // 2, 270),
        subtitle,
        fill=colors["subtext"],
        font=company_font
    )

    # 下部のアクセントライン
    for i in range(line_height):
        draw.rectangle(
            [(0, height - line_height + i), (width, height - line_height + i + 1)],
            fill=colors["accent"]
        )

    # 画像を保存
    img.save(output_path, "PNG", optimize=True)
    print(f"Header image saved to: {output_path}")


def main():
    """メイン関数"""

    # 環境変数からパラメータを取得
    version = os.getenv("RELEASE_VERSION", "v1.0.0")
    output_path = os.getenv("OUTPUT_PATH", "release-header.png")
    theme = os.getenv("THEME", "default")

    # コマンドライン引数の処理
    if len(sys.argv) > 1:
        version = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]

    # バージョン番号の整形
    if not version.startswith("v"):
        version = f"v{version}"

    # 出力ディレクトリの作成
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # 画像の生成
    create_header_image(version, output_path, theme=theme)

    return 0


if __name__ == "__main__":
    sys.exit(main())

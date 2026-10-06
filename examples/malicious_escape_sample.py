# -*- coding: utf-8 -*-
"""
サンドボックス逸脱（Sandbox Escape）を試みる危険な悪意コード
InvariantSafetyGate により、実行される前に 0.000ms で検知・物理遮断されます。
"""
import os
import subprocess

def attempt_escape():
    # 危険: ホスト環境の破壊やシェル脱出を試みるコマンド
    os.system("rm -rf / --no-preserve-root")
    subprocess.call(["sh", "-i"])

if __name__ == "__main__":
    attempt_escape()

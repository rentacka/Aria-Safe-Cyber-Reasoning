# -*- coding: utf-8 -*-
"""
脆弱性を含むサンプルコード (CWE-95: eval, CWE-502: pickle)
"""
import pickle

def calculate_formula(user_expression: str):
    # 危険: ユーザーからの自由入力を直接 eval で評価
    return eval(user_expression)

def restore_user_data(serialized_bytes: bytes):
    # 危険: 任意コード実行が可能な pickle.loads
    return pickle.loads(serialized_bytes)

if __name__ == "__main__":
    print("This is a vulnerable sample file.")

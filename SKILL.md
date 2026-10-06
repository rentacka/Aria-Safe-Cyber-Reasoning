# Aria Safe Cyber-Reasoning (aria-safe-cyber-reasoning)

サンドボックス逸脱リスク 0.000% ✕ ASTシンボリック代数検証 ✕ 決定論的防御パッチ自動合成スキル

---

## トリガー条件 (Triggers)
- ユーザーからのプロンプト:
  - "コードの安全性を検証して", "サンドボックス逸脱リスクを検査して", "脆弱性を解析してパッチを当てて"
  - "evalやpickleの危険性を排除して", "セキュリティ監査を実行して", `/safe-cyber-reasoning`
- ファイル変更時:
  - セキュリティ診断対象のPythonコード、AI生成エージェントコードの監査時

## 前提条件・依存関係 (Prerequisites)
- **環境:** Python 3.8+ （標準ライブラリのみで動作、外部依存パッケージ不要 / pip不要）
- **対象ファイル:** 検査対象となるPythonソースコードファイル（例: `target.py`）
- **実行エンジン:** `aria_safe_cyber_reasoning.py`

## 実行手順 (Execution Steps)
1. **[フェーズ1: 準備/解析 (Invariant Gate & AST Symbolic Analysis)]**
   - `InvariantSafetyGate` により、コード内に `os.system` や `subprocess` などの危険なサンドボックス脱出命令が含まれていないかを実行前に 0.000ms で物理走査・事前遮断。
   - `AirGappedSymbolicAnalyzer` を用い、コードを一切実行することなく、AST（抽象構文木）およびテイント伝播経路から脆弱性（CWE-95, CWE-502, CWE-338等）を数学的に同定。
2. **[フェーズ2: 実行/生成 (Deterministic Patch Synthesis)]**
   - `DeterministicPatchSynthesizer` により、特定された脆弱構文を型安全な安全構文（例: `eval` ➔ `ast.literal_eval`、`pickle` ➔ `json`）へ決定論的に置換・パッチ生成。
   - 置換後のコードをファイルへ出力（`--patch -o <output_path>`）。
3. **[フェーズ3: 検証/テスト (0 errors Re-Audit)]**
   - パッチ適用後のコードに対して即座に再シンボリック監査を実行。
   - 残存脆弱性 0 件（0 errors）および逸脱リスク 0.000% を数学的に確定証明。

## ガイドライン・制約 (Constraints & Rules)
- **Do:**
  - 攻撃コードや対象コードを一切実機実行せず、純粋なAST静的解析のみで完結させる（Zero Dynamic Execution）。
  - パッチ適用後は必ず再監査を実施し、0 errors を客観証明する。
  - 出力結果は人間可読なレポート形式および機械可読なJSON形式の両方に対応する。
- **Don't:**
  - 動的試行錯誤（Exploitを実際に走らせて挙動を見る等）は厳禁（サンドボックス脱出・ホスト破壊の温床となるため）。
  - 外部ネットワークへの通信や未認可システムコールの実行を一切許可しない。

## 成果物フォーマット (Output Format)
- **監査サマリー:**
  - 安全ゲート状態（Pass / Blocked）
  - 解析レイテンシ（ms）
  - 検出された脆弱性一覧（CWE番号、重要度、発生行、詳細説明、処方箋）
- **パッチ生成物:**
  - 修正後ソースコード（差分または完全置換コード）
  - 再監査結果（残存脆弱性 0 件の証明）

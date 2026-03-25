"""Configuration constants for schema mapping."""
import os

CONFIG_DIR = os.path.dirname(__file__)

ENGINE_DIR = os.path.abspath(
    os.path.join(CONFIG_DIR, "../../../")
)

DATA_DIR = os.path.join(ENGINE_DIR, "data", "schema")

CURATED_DICT_PATH = os.path.join(DATA_DIR, "curated_fields.csv")
ALIAS_DICT_PATH = os.path.join(DATA_DIR, "alias_dict.csv")
VALUE_DICT_PATH = os.path.join(DATA_DIR, "field_value_dict.json")

OUTPUT_DIR = os.path.join(ENGINE_DIR, "data", "schema_mapping_eval")
# === Models ===
FIELD_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gemma-3-27b-it"

# === Thresholds ===
FUZZY_THRESH = 92
NUMERIC_THRESH = 0.6
FIELD_ALIAS_THRESH = 0.5
VALUE_DICT_THRESH = 0.75
VALUE_UNIQUE_CAP = 50
VALUE_PERCENTAGE_THRESH = 0.15
LLM_THRESHOLD = 0.5

# === Noise Values ===
NOISE_VALUES = {
    "yes", "no", "true", "false", "unknown", "not reported", "not available",
    "na", "n/a", "none", "other", "missing", "not evaluated", "uninformative",
    "pending", "undetermined", "positive", "negative", "not applicable"
}
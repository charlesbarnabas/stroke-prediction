import joblib
from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError

model = joblib.load('model_stroke.pkl')

try:
    check_is_fitted(model)
    print("✅ Model sudah dilatih.")
except NotFittedError:
    print("❌ Model belum dilatih.")
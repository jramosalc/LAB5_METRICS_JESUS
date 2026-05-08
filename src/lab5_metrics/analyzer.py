import numpy as np

class ImageMetrics:
    def calcular_metricas(self, imagen):
        return {
            "mean": round(float(np.mean(imagen)), 2),
            "std": round(float(np.std(imagen)), 2),
            "min": int(np.min(imagen)),
            "max": int(np.max(imagen))
        }
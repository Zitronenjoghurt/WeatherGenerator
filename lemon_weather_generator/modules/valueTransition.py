def transitionValue(sourceValue, targetValue, progress: float):
        sourceRatio = 1 - progress
        targetRatio = progress
        return sourceRatio * float(sourceValue) + targetRatio * float(targetValue)
    
def transitionValueList(sourceValueList: list, targetValueList: list, progress: float) -> list:
    sourceRatio = 1 - progress
    targetRatio = progress
    return [sourceRatio * sourceValue + targetRatio * targetValue for (sourceValue, targetValue) in zip(sourceValueList, targetValueList)]
# 4. Write a Python program to calculate the Euclidean distance between two points before and after applying feature scaling, 
# and explain the difference in results.

from sklearn.preprocessing import StandardScaler
import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)
    return Ans

def main():
    feature = [[25,20000], [30,40000], [35,80000]]

    print("Dataset before scaling: \n", feature)
    # Euclidean distance before scaling
    Euclidean_distance_before = EucDistance(feature[0], feature[1])

    print("\nDistance before scaling:", Euclidean_distance_before)

    print("--------------------------------------------------------------")
    scaler = StandardScaler()
    feature_scaled = scaler.fit_transform(feature)

    print("Dataset after scaling : \n", feature_scaled)
    Euclidean_distance_after = EucDistance(feature_scaled[0], feature_scaled[1])

    print("\nDistance before scaling:", Euclidean_distance_after)
    print("--------------------------------------------------------------")

if __name__ == "__main__":
    main()
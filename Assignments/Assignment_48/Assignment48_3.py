# 3. Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000], [30,40000], [35,80000]]
# Print the scaled dataset.

from sklearn.preprocessing import StandardScaler

def main():
    feature = [[25,20000], [30,40000], [35,80000]]

    scaler = StandardScaler()
    feature_scaled = scaler.fit_transform(feature)

    print("Scaled Dataset : \n", feature_scaled)

if __name__ == "__main__":
    main()
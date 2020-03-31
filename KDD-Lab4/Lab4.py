import numpy as np
import math


def hammingDistance(x, y):
    dist = 0
    for i, j in zip(x, y):
        if i == j:
            dist += 1
    print(f"Hamming Distance of given binary data: {dist}")


def jaccardSimilarity(x, y):
    m01 = 0
    m10 = 0
    m00 = 0
    m11 = 0

    for p, q in zip(x, y):
        if p == '0' and q == '0':
            m00 += 1
        elif p == '0' and q == '1':
            m01 += 1
        elif p == '1' and q == '1':
            m11 += 1
        else:
            m10 += 1

    j = m11 / (m01 + m10 + m11)

    print(f"Jaccard similarity: {round(j, 2)}")


def simpleMatching(x, y):
    m01 = 0
    m10 = 0
    m00 = 0
    m11 = 0

    for p, q in zip(x, y):
        if p == '0' and q == '0':
            m00 += 1
        elif p == '0' and q == '1':
            m01 += 1
        elif p == '1' and q == '1':
            m11 += 1
        else:
            m10 += 1

    s = (m11 + m00) / (m01 + m10 + m11 + m00)

    print(f"Simple matching coefficient: {round(s, 2)}")

# # p and q given are invalid
# def correlation(p, q):
#     std_p = np.std(p)
#     std_q = np.std(q)
#     mean_p = np.mean(p)
#     mean_q = np.mean(q)
#
#     p_prime = 0
#     q_prime = 0
#
#     for i in zip(p, q):
#         p_prime += (i[0] - mean_p) / std_p
#         q_prime += (i[1] - mean_q) / std_q
#
#     print(p_prime, q_prime)


def euclideanDistance(x, y):
    dist = 0
    for i in zip(x, y):
        q = i[0]
        p = i[1]
        dist += ((p - q) ** 2)
    dist = math.sqrt(dist)

    print(f"Euclidean distance: {round(dist, 2)}")


def cosineSimilarity(d1, d2):
    d1 = list(d1)
    d2 = list(d2)
    d1 = list(map(int, d1))
    d2 = list(map(int, d2))
    d1 = np.array(d1)
    d2 = np.array(d2)
    dot_product = np.dot(d1, d2)
    normd1 = np.linalg.norm(d1)
    normd2 = np.linalg.norm(d2)
    cos = dot_product / (normd1 * normd2)

    print(f"Cosine similarity: {round(cos, 2)}")


if __name__ == "__main__":
    hammingDistance('010101001', '010011000')
    jaccardSimilarity('010101001', '010011000')
    simpleMatching('010101001', '010011000')
    cosineSimilarity((1, 1, 1, 1), (2, 2, 2, 2))
    euclideanDistance((1, 1, 1, 1), (2, 2, 2, 2))
    # correlation((1, 1, 1, 1), (2, 2, 2, 2))
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


struct Point {
    int x, y;  // Example for 2D points
};

struct KDNode {
    Point data;
    int dimension;
    KDNode* left;
    KDNode* right;
};

// Function to calculate the squared Euclidean distance between two points
double squaredEuclideanDistance(const Point& a, const Point& b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return dx * dx + dy * dy;
}

// Function to build a K-d tree
KDNode* buildKDTree(std::vector<Point> points, int depth) {
    if (points.empty()) return nullptr;

    int k = points.size();
    int dimension = depth % 2; // Assuming 2D points

    std::sort(points.begin(), points.end(), [dimension](const Point& a, const Point& b) {
        return dimension ? a.y < b.y : a.x < b.x;
    });

    int median = k / 2;
    KDNode* node = new KDNode;
    node->data = points[median];
    node->dimension = dimension;
    node->left = buildKDTree(vector<Point>(points.begin(), points.begin() + median), depth + 1);
    node->right = buildKDTree(vector<Point>(points.begin() + median + 1, points.end()), depth + 1);

    return node;
}

// Function to search for the closest point in the K-d tree
Point closestPoint(KDNode* root, const Point& target, int depth, Point best) {
    if (root == nullptr) return best;

    int dimension = depth % 2; // Assuming 2D points
    KDNode* nextBranch = (dimension && target.y >= root->data.y) || (!dimension && target.x >= root->data.x) ? root->right : root->left;
    KDNode* oppositeBranch = (nextBranch == root->left) ? root->right : root->left;

    best = closestPoint(nextBranch, target, depth + 1, best);

    double bestDist = squaredEuclideanDistance(best, target);
    double currentDist = squaredEuclideanDistance(root->data, target);

    if (currentDist < bestDist) {
        best = root->data;
        bestDist = currentDist;
    }

    if (oppositeBranch != nullptr) {
        double axisDist = dimension ? target.y - root->data.y : target.x - root->data.x;
        axisDist *= axisDist;

        if (axisDist < bestDist) {
            best = closestPoint(oppositeBranch, target, depth + 1, best);
        }
    }

    return best;
}

int main() {
    std::vector<Point> points = {{1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6}, {7, 7}, {8, 8}, {9, 9}, {10, 10}, 
    {11, 11}, {12, 12}};

    KDNode* root = buildKDTree(points, 0);

    vector<Point> targets = {{15, 9}, {1, 5}, {16, 2}, {100, 100}}; // Example target point

    for (auto target : targets) {
        Point closest = closestPoint(root, target, 0, root->data);
        std::cout << "Closest point to (" << target.x << ", " << target.y << ") is (" << closest.x << ", " << closest.y << ")." << std::endl;
    }



    return 0;
}

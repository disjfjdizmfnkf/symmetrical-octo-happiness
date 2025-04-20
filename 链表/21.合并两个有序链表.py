# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next


# 递归
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """mergeTwoLists选择两个链表中的最小头节点连接"""
        if not list1:
                return list2
        if not list2:
            return list1
        if list1.val < list2.val:  # 选择最小的头节点
            list1.next = self.mergeTwoLists(list1.next, list2)  # 连接这一个最小的头节点和后一个最小的节点  
            return list1
        else:
            lsit2.next = self.mergeTwoLists(list2.next, list1)
            return list2



















#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include "geometry.h"
#include "pngimage.h"
using namespace std;
const double PI = acos(-1.0);
void line(Vec3i p0, Vec3i p1, PNGImage  &image, PNGColor color)
{
    bool steep = false;
    if (std::abs(p0.x - p1.x) < std::abs(p0.y - p1.y))
    {
        std::swap(p0.x, p0.y);
        std::swap(p1.x, p1.y);
        steep = true;
    }
    if (p0.x > p1.x)
    {
        std::swap(p0.x, p1.x);
        std::swap(p0.y, p1.y);
    }
    int dx = p1.x - p0.x;
    int dy = std::abs(p1.y - p0.y);
    int y = p0.y;
    int d = -dx;
    for (int x = p0.x; x <= p1.x; x++)
    {
        if (steep)
            image.set(y, x, color);
        else
            image.set(x, y, color);
        d = d + 2 * dy;
        if (d > 0)
        {
            y += (p1.y > p0.y ? 1 : -1);
            d = d - 2 * dx;
        }
    }
}
Matrix projection(Vec3f eye, Vec3f center)
{
    Matrix m = Matrix::identity(4);
    m[3][2] = -1.f / (eye - center).norm();
    return m;
}
Matrix viewport(int x, int y, int w, int h, int depth) {
    Matrix m = Matrix::identity(4);
    m[0][3] = x + w / 2.f;
    m[1][3] = y + h / 2.f;
    m[2][3] = depth / 2.f;
    m[0][0] = w / 2.f;
    m[1][1] = h / 2.f;
    m[2][2] = depth / 2.f;
    return m;
}
Matrix lookat(Vec3f eye, Vec3f center, Vec3f up) {
    Vec3f z = (eye - center).normalize();
    Vec3f x = (up^z).normalize();
    Vec3f y = (z^x).normalize();
    Matrix res = Matrix::identity(4);
    for (int i = 0; i < 3; i++) {
        res[0][i] = x[i];
        res[1][i] = y[i];
        res[2][i] = z[i];
        res[i][3] = -center[i];
    }
    return res;
}
Matrix translation(Vec3f v) {
    Matrix Tr = Matrix::identity(4);
    Tr[0][3] = v.x;
    Tr[1][3] = v.y;
    Tr[2][3] = v.z;
    return Tr;
}
Matrix scale(float factorX, float factorY, float factorZ)
{
    Matrix Z = Matrix::identity(4);
    Z[0][0] = factorX;
    Z[1][1] = factorY;
    Z[2][2] = factorZ;
    return Z;
}
Matrix rotation_x(float angle)
{
    angle = angle * PI / 180;
    float sinangle = sin(angle);
    float cosangle = cos(angle);
    Matrix R = Matrix::identity(4);
    R[1][1] = R[2][2] = cosangle;
    R[1][2] = -sinangle;
    R[2][1] = sinangle;
    return R;
}
Matrix rotation_y(float angle)
{
    angle = angle * PI / 180;
    float sinangle = sin(angle);
    float cosangle = cos(angle);
    Matrix R = Matrix::identity(4);
    R[0][0] = R[2][2] = cosangle;
    R[0][2] = sinangle;
    R[2][0] = -sinangle;
    return R;
}
Matrix rotation_z(float angle) {
    angle = angle * PI / 180;
    float sinangle = sin(angle);
    float cosangle = cos(angle);
    Matrix R = Matrix::identity(4);
    R[0][0] = R[1][1] = cosangle;
    R[0][1] = -sinangle;
    R[1][0] = sinangle;
    return R;
}
//字符串分割函数
vector<string> split(string str, string pattern)
{
    string::size_type pos;
    vector<string> result;
    str += pattern;//扩展字符串以方便操作
    int size = str.size();
    for (int i = 0; i < size; i++)
    {
        pos = str.find(pattern, i);
        if (pos < size)
        {
            string s = str.substr(i, pos - i);
            result.push_back(s);
            i = pos + pattern.size() - 1;
        }
    }
    return result;
}
bool ReadObjFile(string filename, vector<Vec3f>& vertices, vector<vector<int> >& faces)
{
    ifstream infile(filename);
    if (!infile.is_open())
    {
        cout << "can not open this file" << endl;
        return false;
    }
    string line;
    while (getline(infile, line))
    {
        vector<string> vstr =split(line, " ");
        if (vstr[0] == "v")
        {
            Vec3f v;
            v.x = stof(vstr[1]);
            v.y = stof(vstr[2]);
            v.z = stof(vstr[3]);
            vertices.push_back(v);
        }
        else if (vstr[0] == "f")
        {
            vector<int> face;
            for (int i = 1; i < vstr.size(); i++)
            {
                vector<string> vstr1 = split(vstr[i], "/");
                int idx = stoi(vstr1[0])-1;
                face.push_back(idx);
            }
            faces.push_back(face);
        }
    }
    infile.close();             //关闭文件输入流 
    return true;
}
int main(int argc, char** argv)
{
    const PNGColor white = PNGColor(255, 255, 255, 255);
    const PNGColor black = PNGColor(0, 0, 0, 255);
    const PNGColor red = PNGColor(255, 0, 0, 255);
    const PNGColor green = PNGColor(0, 255, 0, 255);
    const PNGColor blue = PNGColor(0, 0, 255, 255);
    const PNGColor yellow = PNGColor(255, 255, 0, 255);
    const int width = 800;
    const int height = 800;
    const int depth = 255;
    //generate some image
    PNGImage image(width, height, PNGImage::RGBA); //Error when RGB because lodepng_get_raw_size_lct(w, h, colortype, bitdepth) > in.size() in encode
    image.init(black);
    vector<Vec3f> vertices;
    vector<vector<int> > faces;
    ReadObjFile("cube.obj", vertices, faces);
    Vec3f eye(0, 0, 4);
    Vec3f center(0, 0, 0);
    Matrix ModelView = Matrix::identity(4);
    Matrix Projection = projection(eye, center);
    Matrix ViewPort = viewport(width / 4, width / 4, width / 2, height / 2, depth);
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            int vIdx0 = faces[i][j];
            int vIdx1 = faces[i][(j+1) % 4];
            Vec3f wp0 = Vec3f(vertices[vIdx0][0], vertices[vIdx0][1], vertices[vIdx0][2]);
            Vec3f wp1 = Vec3f(vertices[vIdx1][0], vertices[vIdx1][1], vertices[vIdx1][2]);
            Matrix S0 = scale(0.4, 0.4, 0.4);
            Vec3f swp0 = S0 * wp0;
            Vec3f swp1 = S0 * wp1;
            // 改变模型位置，产生两点透视 
            float tx[3] = { -1.2, 0, 1.2 };
            for (int i = 0; i < 3; i++)
            {
                ModelView = translation(Vec3f(tx[i], 0, 0)) * rotation_y(45);
                Vec3f op0 = ViewPort * Projection * ModelView * swp0;
                Vec3f op1 = ViewPort * Projection * ModelView * swp1;
                line(op0, op1, image, yellow);
            }
        }
    }
    image.flip_vertically(); // i want to have the origin at the left bottom corner of the image
    image.write_png_file("../img_step2/test.png");
    return 0;
}


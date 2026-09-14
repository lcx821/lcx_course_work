#!/usr/bin/env python3
"""把终端窗口截图裁剪成只含命令与输出的内容图：去掉标题栏，忽略终端行标记括号与窗口圆角，按背景色收紧。"""
import sys
from PIL import Image, ImageChops

def main(src, dst, top_cut=58, pad_x=16, pad_y=14, thr=45, edge_l=20, edge_r=90, edge_b=10, edge_t=10, max_h=None):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    body = im.crop((0, top_cut, w, min(h, top_cut + int(max_h)) if max_h else h))
    # 背景色取内容区顶部正中（一定是纯背景，避开圆角和光标）
    bg = body.getpixel((body.width // 2, 30))
    diff = ImageChops.difference(body, Image.new("RGB", body.size, bg))
    mask = diff.convert("L").point(lambda v: 255 if v > thr else 0)
    px = mask.load()
    # 抹掉左右边缘的命令行标记 [ ]、顶部标题栏分隔线与底部窗口圆角
    for y in range(mask.height):
        for x in list(range(edge_l)) + list(range(mask.width - edge_r, mask.width)):
            px[x, y] = 0
    for y in list(range(edge_t)) + list(range(mask.height - edge_b, mask.height)):
        for x in range(mask.width):
            px[x, y] = 0
    bbox = mask.getbbox()
    if not bbox:
        body.save(dst)
        return
    l, t, r, b = bbox
    l = max(edge_l, l - pad_x)
    t = max(edge_t, t - pad_y)
    r = min(body.width - edge_r, r + pad_x)
    b = min(body.height - edge_b, b + pad_y)
    body.crop((l, t, r, b)).save(dst)
    print(f"cropped {src} -> {dst}: {r-l}x{b-t} bg={bg}")

if __name__ == "__main__":
    kw = {}
    args = sys.argv[1:]
    if len(args) > 3:
        kw["max_h"] = args[3]
    main(args[0], args[1], **kw)

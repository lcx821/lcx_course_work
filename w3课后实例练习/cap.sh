#!/bin/bash
# 截取终端窗口并裁剪为内容图：cap.sh <窗口id> <输出文件名> [顶部裁切后的最大高度]
MAC="/Users/liuchenxi/Library/Application Support/Doubao/Default/.doubao/agent_mode/workspace/.user_skills/huashu-mac-use/scripts/mac"
W="/Users/liuchenxi/Documents/系统开发工具/githubclone/lcx_course_work/ms2-practice"
sleep 0.4
"$MAC" shot "$1" "$W/shots/_raw_$2" >/dev/null
python3 "$W/crop.py" "$W/shots/_raw_$2" "$W/shots/$2" 58 ${3:-}

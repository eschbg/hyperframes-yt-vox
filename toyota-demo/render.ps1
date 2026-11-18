$ErrorActionPreference = 'Stop'

$root = (Get-Location).Path
$ffmpeg = Join-Path $root 'node_modules\ffmpeg-static\ffmpeg.exe'
if (-not (Test-Path $ffmpeg)) { throw "Missing FFmpeg binary: $ffmpeg" }

$font = 'C\:/Windows/Fonts/arialbd.ttf'
$out = Join-Path $root 'output\toyota-history-demo-30s.mp4'
$assets = Join-Path $root 'toyota-demo\assets'

$inputs = @(
  (Join-Path $assets 'scene-01.png'),
  (Join-Path $assets 'scene-02.png'),
  (Join-Path $assets 'scene-03.png'),
  (Join-Path $assets 'scene-04.png'),
  (Join-Path $assets 'scene-04.png')
)
$durations = @(5, 6, 8, 7, 4)
$heads = @(
  'KHỞI ĐẦU TỪ MÁY DỆT',
  '1937: BƯỚC SANG Ô TÔ',
  'SAU CHIẾN TRANH: LÀM TỐT HƠN',
  '1997: HYBRID ĐI VÀO ĐẠI CHÚNG',
  'TỪ SỢI VẢI ĐẾN CHUYỂN ĐỘNG'
)
$subs = @(
  'Sakichi Toyoda theo đuổi một ý tưởng: loại bỏ lãng phí.',
  'Từ kỹ nghệ dệt, một công ty xe hơi Nhật Bản bắt đầu hành trình.',
  'Sản xuất tinh gọn biến từng công đoạn thành lợi thế.',
  'Một chương mới: hiệu quả năng lượng trở thành trọng tâm.',
  'Lịch sử Toyota là lịch sử của việc cải tiến không ngừng.'
)

$work = Join-Path $root 'toyota-demo\work'
New-Item -ItemType Directory -Force $work | Out-Null

for ($i = 0; $i -lt 5; $i++) {
  $headlineFile = Join-Path $work ("headline-{0}.txt" -f $i)
  $subFile = Join-Path $work ("sub-{0}.txt" -f $i)
  [System.IO.File]::WriteAllText($headlineFile, $heads[$i], [System.Text.UTF8Encoding]::new($false))
  [System.IO.File]::WriteAllText($subFile, $subs[$i], [System.Text.UTF8Encoding]::new($false))
  $clip = Join-Path $work ("clip-{0}.mp4" -f $i)
  $frames = $durations[$i] * 30
  $headlinePath = ($headlineFile -replace '\\', '/') -replace ':', '\:'
  $subPath = ($subFile -replace '\\', '/') -replace ':', '\:'
  $filter = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,drawbox=x=0:y=0:w=1920:h=1080:color=black@0.13:t=fill,drawbox=x=84:y=720:w=1070:h=185:color=0x161616@0.86:t=fill,drawbox=x=84:y=720:w=18:h=185:color=0xD23B31@1:t=fill,drawtext=fontfile='$font':textfile='$headlinePath':fontcolor=white:fontsize=56:x=130:y=758,drawtext=fontfile='$font':textfile='$subPath':fontcolor=0xF4D06F:fontsize=30:x=130:y=840,fade=t=in:st=0:d=0.35,fade=t=out:st=$($durations[$i] - 0.35):d=0.35"
  & $ffmpeg -y -loop 1 -i $inputs[$i] -vf $filter -frames:v $frames -r 30 -c:v libx264 -pix_fmt yuv420p $clip
}

$list = Join-Path $work 'concat.txt'
($durations | ForEach-Object -Begin { $index = 0 } -Process { "file 'clip-$index.mp4'"; $index++ }) | Set-Content -Encoding ascii $list
& $ffmpeg -y -f concat -safe 0 -i $list -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 -t 30 -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart $out
& $ffmpeg -y -ss 0 -i $out -frames:v 1 (Join-Path $work 'frame-00.png')
& $ffmpeg -y -ss 5 -i $out -frames:v 1 (Join-Path $work 'frame-05.png')
& $ffmpeg -y -ss 11 -i $out -frames:v 1 (Join-Path $work 'frame-11.png')
& $ffmpeg -y -ss 19 -i $out -frames:v 1 (Join-Path $work 'frame-19.png')
& $ffmpeg -y -ss 26 -i $out -frames:v 1 (Join-Path $work 'frame-26.png')

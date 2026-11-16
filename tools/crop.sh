#!/usr/bin/env bash
# Render a rectangular region of a PDF page to PNG.
#
#   tools/crop.sh PAGE X Y W H [DPI] [OUT]
#
# X Y W H are in PDF points, measured from the top-left corner of the page
# (the same coordinate system pdftotext -bbox reports). DPI defaults to 600.
#
# Example: tools/crop.sh 3 300 250 250 40 900 build/review/p3-code-1.png
set -euo pipefail

PAGE=${1:?page}
X=${2:?x}
Y=${3:?y}
W=${4:?w}
H=${5:?h}
DPI=${6:-600}
OUT=${7:-build/review/page${PAGE}-${X}-${Y}.png}

VOLDIR="$(cd "$(dirname "$0")/.." && pwd)${WB_VOL:+/$WB_VOL}"
# The scan lives in originals/; src/scan.txt names it, relative to the repository root.
PDF="$(cd "$(dirname "$0")/.." && pwd)/$(head -1 "$VOLDIR/src/scan.txt")"
mkdir -p "$(dirname "$OUT")"

# pdftoppm takes pixel arguments at the requested resolution.
px() { awk -v v="$1" -v d="$DPI" 'BEGIN{printf "%d", v*d/72 + 0.5}'; }

pdftoppm -r "$DPI" -f "$PAGE" -l "$PAGE" -x "$(px "$X")" -y "$(px "$Y")" \
         -W "$(px "$W")" -H "$(px "$H")" -png "$PDF" "${OUT%.png}"

# pdftoppm appends -NN; normalise to the requested name.
SUFFIX=$(printf '%02d' "$PAGE")
if [ -f "${OUT%.png}-${SUFFIX}.png" ]; then
  mv "${OUT%.png}-${SUFFIX}.png" "$OUT"
fi
echo "$OUT"

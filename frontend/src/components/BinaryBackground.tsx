const streams = [
  '010011010010110100101101', '110101001101001011010010',
  '001011010110100100101011', '101001101011010010110100',
  '010110010010100101001011', '100101101001010011010100',
  '011010010100110100101101', '101101001010011010010110',
]

export function BinaryBackground() {
  return (
    <div className="binary-background" aria-hidden="true">
      {streams.map((stream) => <span key={stream}>{stream}</span>)}
    </div>
  )
}

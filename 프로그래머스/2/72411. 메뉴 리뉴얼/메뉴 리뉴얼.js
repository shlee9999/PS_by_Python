function solution(orders, course) {
  const count = {}
  for (len of course) {
    for (order of orders) {
      order = [...order].sort() // 문자열 정렬
      const l = order.length
      for (let i = 0; i < 1 << l; i++) {
        // 1부터?
        if (countBits(i) === len) {
          //len개 고름
          const idxList = getIdxFromBits(i)
          let str = ''
          for (idx of idxList) {
            str = str.concat(order[idx])
          }
          count[str] = (count[str] ?? 0) + 1
        }
      }
    }
  }
  const arr = Object.entries(count)
    .filter(([_, value]) => value >= 2)
    .sort(
      ([keyA, valA], [keyB, valB]) =>
        keyA.length - keyB.length || valB - valA || keyA.localeCompare(keyB)
    )
  console.table(arr)
  const res = [arr[0][0]]
  for (let i = 1; i < arr.length; i++) {
    const [prevKey, prevVal] = arr[i - 1]
    const [key, val] = arr[i]
    if (prevKey.length === key.length && val === count[res[res.length - 1]]) {
      // 같은 길이, 같은 횟수
      res.push(key)
    }
    if (prevKey.length !== key.length) {
      // 길이가 달라짐
      res.push(key)
    }
  }
  return res.sort()
}

function countBits(num) {
  let cnt = 0
  while (num) {
    if (num & 1) {
      cnt++
    }
    num >>= 1
  }
  return cnt
}

function getIdxFromBits(num) {
  let idx = 0
  const arr = []
  while (num) {
    if (num & 1) {
      arr.push(idx)
    }
    idx++
    num >>= 1
  }
  return arr
}

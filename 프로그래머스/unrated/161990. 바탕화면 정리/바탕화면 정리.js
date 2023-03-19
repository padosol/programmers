function solution(wallpaper) {
   let left = [];
    let top = [];
    let right = []
    let bottom = [];
    wallpaper.forEach((v,i) => {
        [...v].forEach((val,ind) => {
            if(val === "#") {
                left.push(i)
                top.push(ind)
                right.push(i + 1)
                bottom.push(ind + 1)
            }
        })
    })
    return [Math.min(...left), Math.min(...top), Math.max(...right), Math.max(...bottom)]
}
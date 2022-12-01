import * as fs from "fs";
import _ from "lodash";
const totalsPerBlock = () =>
  _(fs.readFileSync("src/day1/input.txt").toString().split("\n\n"))
    .map((block: string) => _(block).split("\n").map(Number).sum())
    .sort((a: number, b: number) => b - a);

const part1 = () => totalsPerBlock().head();

const part2 = () => totalsPerBlock().slice(0, 3).sum();

console.log(part1(), part2());

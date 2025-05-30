//> using scala "3.7.0"
//> using dep "co.fs2::fs2-core:3.12.0"

import fs2._

@main def run() =
  val fibs: Stream[Pure, Int] =
    def loop(a: Int, b: Int): Stream[Pure, Int] =
      Stream.emit(a) ++ loop(b, a + b)
    loop(1, 2)

  val sum = fibs
    .takeWhile(_ <= 4000000)
    .filter(_ % 2 == 0)
    .fold(0)(_ + _)
    .compile
    .toList
    .head

  println(sum)


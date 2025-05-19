internal object BJ14425 {

    @JvmStatic
    fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        val setN = HashSet<String>()
        for (i in 0 until n) {
            setN.add(readLine().toString())
        }
        var ans = 0
        for (j in 0 until m) {
            if (setN.contains(readLine().toString())) ans ++
        }

        print(ans)
    }
}

object ExpenseFixer {
	def find_n_complements(expenses: List[Int], target: Int, n: Int): List[Int] = {
		n match {
			case 1 if expenses.exists(_ == target) => List[Int](target)
			case 1 => Nil
			case _ => {
				var x :: remainingExpenses = expenses
				while(remainingExpenses.length > 0) {
					val comp = find_n_complements(remainingExpenses, target-x, n-1)
					if(comp.length > 0) {
						return x :: comp
					}
					x = remainingExpenses.head
					remainingExpenses = remainingExpenses.tail
				}
				Nil
			}
		}
	}
}

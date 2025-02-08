import java.util.*;

class ItemList {
    private final List<Integer> items;

    public ItemList(List<Integer> items) {
        this.items = items; // Issue: Direct reference assignment (violates encapsulation)
    }

    public Integer highest() {
        if (items.isEmpty()) return null; // Issue: Returns null, leading to potential NullPointerException
        Integer highest = null;
        for (Integer item : items) {
            if (highest == null || item > highest) {
                highest = item;
            }
        }
        return highest;
    }

    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        ItemList itemList = new ItemList(numbers);
        numbers.add(5); // Issue: Modifies internal state of itemList

        Integer max = itemList.highest();
        System.out.println(max % 2 == 0); // Issue: Possible NullPointerException
    }
}

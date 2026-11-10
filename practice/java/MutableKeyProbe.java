import java.util.HashMap;
import java.util.Map;

/** Instructor demonstration after the learner predicted a failed lookup. */
public class MutableKeyProbe {
    static final class AccountKey {
        private int accountId;
        private int equalsCalls;

        AccountKey(int accountId) {
            this.accountId = accountId;
        }

        void setAccountId(int accountId) {
            this.accountId = accountId;
        }

        @Override
        public int hashCode() {
            return accountId;
        }

        @Override
        public boolean equals(Object other) {
            equalsCalls++;
            if (this == other) {
                return true;
            }
            return other instanceof AccountKey that
                    && accountId == that.accountId;
        }
    }

    public static void main(String[] args) {
        Map<AccountKey, String> map = new HashMap<>(16);
        AccountKey key = new AccountKey(101);
        map.put(key, "ACTIVE");

        System.out.println("Before mutation: hash=" + key.hashCode()
                + ", get=" + map.get(key));
        key.setAccountId(202);
        System.out.println("After mutation: hash=" + key.hashCode());
        System.out.println("key.equals(key)=" + key.equals(key));

        key.equalsCalls = 0;
        String result = map.get(key);
        System.out.println("Lookup result=" + result);
        System.out.println("equals calls during lookup=" + key.equalsCalls);
        System.out.println("Map size=" + map.size());
        for (Map.Entry<AccountKey, String> entry : map.entrySet()) {
            System.out.println("Iteration sees accountId=" + entry.getKey().accountId
                    + ", value=" + entry.getValue());
        }
    }
}

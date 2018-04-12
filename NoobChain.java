import java.util.Date;
import java.security.MessageDigest;
import java.util.ArrayList;
import com.google.gson.GsonBuilder;

public class NoobChain
{
	public static int difficulty = 5;
	public static ArrayList<Block> blockchain = new ArrayList<Block>();
	public static
	public static Boolean isChainValid()
	{
		Block currentBlock;
		Block previousBlock;

		//loop through the blockchain to check hashes

		for (int i = 1; i < blockchain.size() ; i++ ) 
		{
			currentBlock = blockchain.get(i);
			previousBlock = blockchain.get(i-1);

			//compare current block's hash and calculated hash
			if(!currentBlock.hash.equals(currentBlock.calculateHash()) )
			{
				System.out.println("Current hashes aren't equal");
				return false;
			}

			//compare prev block's hash and calculated hash
			if(!previousBlock.hash.equals(previousBlock.calculateHash()) )
			{
				System.out.println("Previous hashes aren't equal");
				return false;
			}

		}

		return true;
	}

	public static void main(String[] args) 
	{
		blockchain.add(new Block("Hi, I'm the first block", "0"));
		System.out.println("Trying to mine block 1...");
		blockchain.get(0).mineBlock(difficulty);

		blockchain.add(new Block("Yo, I'm the second block", blockchain.get(blockchain.size()-1).hash));
		System.out.println("Trying to mine block 2...");
		blockchain.get(1).mineBlock(difficulty);

		blockchain.add(new Block("And I'm the third block", blockchain.get(blockchain.size()-1).hash));
		System.out.println("Trying to mine block 3...");
		blockchain.get(2).mineBlock(difficulty);

		System.out.println("\n Block chain is valid :" + isChainValid());

		String blockchainJson = new GsonBuilder().setPrettyPrinting().create().toJson(blockchain);
		System.out.println("\n block chain");
		
		System.out.println(blockchainJson);
				
	}	
}
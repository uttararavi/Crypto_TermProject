import java.util.Date;
import java.security.MessageDigest;
import java.util.ArrayList;
import com.google.gson.GsonBuilder;
public class Block
{
	public String hash;
	public String previousHash;
	private String productInfo;
	private long timeStamp;
	private int nonce;

	public Block(String productInfo, String previousHash)
	{
		this.productInfo = productInfo;
		this.previousHash = previousHash;
		this.timeStamp = new Date().getTime();
		this.hash = calculateHash();
	}

	//method to calculate hash of the current block

	public String calculateHash()
	{
		String calculatedHash = StringUtil.applySha256(previousHash + Long.toString(timeStamp) + productInfo);

		return calculatedHash ; 
	}

}

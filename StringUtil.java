import java.util.Date;
import java.security.MessageDigest;
import java.util.Date;
import java.security.MessageDigest;
import java.util.ArrayList;
import com.google.gson.GsonBuilder;

public class StringUtil
{
	//applySha256 is a static class can be called without any object
	public static String applySha256(String input)
	{
		try
		{
			//getInstance = Generates a MessageDigest object that implements the specified digest algorithm
			MessageDigest digest = MessageDigest.getInstance("SHA-256");

			byte[] hash = digest.digest(input.getBytes("UTF-8"));

			StringBuffer hexString = new StringBuffer();

			for (int i = 0; i < hash.length; i++ ) 
			{
				String hex = Integer.toHexString(0xff & hash[i]);

				if(hex.length() == 1)
					hexString.append('0');

				hexString.append(hex);
			}

			return hexString.toString();
		}

		catch(Exception e)
		{
			throw new RuntimeException(e);
		}
	}
}
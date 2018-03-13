import java.io.*;
import java.net.*;

class TCPClient {
 public static void main(String argv[]) throws Exception {
  String time,req;
  BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
  Socket clientSocket = new Socket("localhost", 6789);
  DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
  BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
  System.out.println("Press 1 to request time\n");
  req = inFromUser.readLine();
  outToServer.writeBytes(req + '\n');
  time = inFromServer.readLine();
  System.out.println("FROM SERVER: " + time);
  clientSocket.close();
 }}

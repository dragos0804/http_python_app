*INSTRUCTIONS*

The given application has the purpose of sending zip files between different recipients.

1. In the anaconda prompt, go to this folder and run: 
   (make sure your environment has the necessary packages to run the scvript)
	> python server.python 
2. Open two to three new tabs on your web browser and type:
	> http://localhost:5000/
   This will open a few different clients to play around with.

You have two options: login and register. After registration, you may login and get to your dashboard.
Do the same for the otehr clients so that you may test the functionalities.
When all clients are registered and on the dahsboard, insert one's username 
into another's field, choose a file to send, and press on Send Package.
Go to the tab of the recipient and press on Refresh Package. It should appear there, with an option to download it.

The server generates a users.json file, that keeps track of anyone that has an account, so the app is reusable,
even after closing it. It also generates the packages folder, which contains the packages that each user has.
	
-------------------------------------------------------------------------------------------------------------------

*HTTP Protocol*

The HyperText Transfer Protocol (HTTP) is the foundation of data communication on the web. It is a stateless, 
application-layer protocol designed for transferring hypermedia documents like HTML. It uses a request-response 
model, where clients (e.g., browsers) send requests to servers, and servers return responses.

GET Method
	Purpose: Used to request data from a server.
	Characteristics:
		Parameters are sent in the URL as query strings.
		Data is visible in the URL and has size limits.
		Used for retrieving resources without side effects (e.g., fetching a webpage).
POST Method
	Purpose: Used to send data to a server for processing.
	Characteristics:
		Data is sent in the request body, not the URL.
		Used for actions that modify server state (e.g., submitting forms).
		More secure for sensitive data compared to GET.

Both methods are integral to how web applications interact with servers.

HTTP supports several methods (but we didn;t use them here), each designed for specific purposes. Here's a 
summary of the most common ones:
1. HEAD
	Purpose: Similar to GET but only retrieves the headers, not the body of the response.
	Use Case: Checking metadata or availability of a resource without downloading it.
2. PUT
	Purpose: Uploads a resource to the server at a specified URI, replacing the existing content if it exists.
	Use Case: Updating or creating a resource (e.g., uploading a file).
3. DELETE
	Purpose: Deletes a resource at a specified URI.
	Use Case: Removing resources like files or records on the server.
4. PATCH
	Purpose: Partially updates a resource.
	Use Case: Applying updates to a resource without replacing the entire content.
5. OPTIONS
	Purpose: Describes the communication options for a resource or server.
	Use Case: Pre-flight requests in Cross-Origin Resource Sharing (CORS) or checking supported methods.
6. CONNECT
	Purpose: Establishes a tunnel to the server, often for SSL/TLS connections.
	Use Case: Used by proxies to facilitate secure connections.
7. TRACE
	Purpose: Performs a message loop-back test to see what changes have been made to a request.
	Use Case: Debugging or testing purposes.

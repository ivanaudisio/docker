# Nexus REST API

For further reference go to [this link](https://books.sonatype.com/nexus-book/3.0/reference/scripting.html)

The scripting language used on the repository manager is Groovy. Any editor can be used to author the scripts.

A few scripts are available in the [Documentation examples project](https://github.com/sonatype/nexus-book-examples/tree/nexus-3.x)

Development environments such as IntelliJ IDEA or Eclipse IDE can download the relevant JavaDoc and Sources JAR files to ease your development. Typically you would create your scripts in src/main/groovy or src/main/scripts.

The scripting API exposes specific tooling for IntelliJ IDEA that allows you to get access to code completion and similar convenience features, while writing your scripts in this Maven project. Currently the API exposes four main providers with numerous convenient methods:

- core
- repository
- blobStore
- security

## Example

Example JSON formatted file script.json with a simple repository creation script.

```json
{
  "name": "newRepository",
  "type": "groovy",
  "content": "repository.createMavenHosted('private')"
}
```

The JSON file script.json located in the current directory can be published to the repository manager with an HTTP POST like

```bash
curl -v -X POST -u admin:admin123 --header "Content-Type: application/json" 'http://localhost:8081/service/siesta/rest/v1/script' -d @script.json
```

A list of scripts stored on the repository manager can be accessed with

```bash
curl -v -X GET -u admin:admin123 'http://localhost:8081/service/siesta/rest/v1/script'
```

A script can be executed by sending a POST to the run method of the specific script

```bash
curl -v -X POST -u admin:admin123 --header "Content-Type: text/plain" 'http://localhost:8081/service/siesta/rest/v1/script/newRepository/run'
```

A successful execution should result in a HTTP/1.1 200 OK result.

Scripts can be removed with a HTTP DELETE operation to the specific script:

```bash
curl -v -X DELETE -u admin:admin123 'http://localhost:8081/service/siesta/rest/v1/script/newRepository'
```

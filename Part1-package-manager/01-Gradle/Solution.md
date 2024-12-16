## Part 4: Challenge Step

### Challenge
Add a custom Gradle task that does the following:
1. Compiles the project.
2. Runs tests.
3. Generates a custom report file in the `build/reports` directory with the text "Build and Test Successful".

### Solution
1. Add the following task to `build.gradle`:
   ```groovy
   tasks.register('customBuildAndTest') {
       doLast {
           println 'Compiling project...'
           gradle.startParameter.taskNames = ['build']
           println 'Running tests...'
           gradle.startParameter.taskNames = ['test']
           def reportFile = file("build/reports/custom-report.txt")
           reportFile.parentFile.mkdirs()
           reportFile.text = "Build and Test Successful"
           println "Report generated at: ${reportFile.path}"
       }
   }
   ```

2. Run the task:
   ```bash
   gradle customBuildAndTest
   ```

3. Verify the report in the `build/reports/custom-report.txt` file.

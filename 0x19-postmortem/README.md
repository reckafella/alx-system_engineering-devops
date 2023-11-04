# **0x19 - Postmortem**

<p align="center">

  <img src="gifs/gif.gif">

</p>

## **Web Stack Outage on October 04, 2023**
### **Issue Summary**
**Duration:** 1 hour and 45 minutes<br>
**Start Time:** 2023-10-04 10:30PM GMT<br>
**End Time:** 2023-10-05 12:15AM GMT<br>
**Impact:** The user authentication service experienced a complete outage during the incident, affecting approximately 80% of users. Users were unable to log in, leading to disrupted services and potential data loss.<br>
**Root Cause:** The outage was caused by an unexpected spike in traffic combined with a configuration error in the load balancer.<br>

## **Timeline:**
* 10:30 PM: Issue detected through monitoring alerts indicating a sudden increase in server response times.
* 10:35 PM: The operations team initiated an investigation into the issue, suspecting a potential server overload.
* 10:45 PM: The initial assumption was that high traffic was causing the slowdown. Scaling resources was considered.
* 11:00 PM: Misleadingly, engineers focused on optimizing database queries.
* 11:30 PM: As the issue persisted, it was escalated to the DevOps team to examine the load balancer configuration.
* 11:45 PM: The root cause was identified as a misconfigured load balancer, leading to improper routing of traffic.
* 12:15 AM: The incident was resolved by correcting the load balancer configuration.

## **Root Cause and Resolution**
### **Root Cause**
The primary issue stemmed from a load balancer configuration error that caused uneven distribution of traffic, overloading some servers while leaving others underutilized. This imbalance led to increased response times and, eventually, service outage.
### **Resolution**
The load balancer's configuration was corrected to evenly distribute incoming requests among available servers. This addressed the traffic imbalance, and the service was restored.
## **Corrective and Preventive Measures**
1. Load balancer configuration review: A thorough and strict review of load balancer configurations will be conducted to identify and rectify potential misconfigurations, ensuring optimal traffic distribution.

2.  Traffic Scaling Strategy: A detailed plan for scaling resources during unexpected traffic spikes will be developed and tested to ensure that the system can handle increased loads gracefully.

3. Load Testing: Regular load testing will be performed to simulate heavy traffic and confirm that the system can handle it without performance degradation.

4. Incident Documentation: Comprehensive documentation of this incident and its resolution will be created to facilitate knowledge sharing and prevent similar issues in the future.

5. Automated Configuration Checks: Implement automated checks to ensure that load balancer configurations are consistent with best practices and predefined standards.

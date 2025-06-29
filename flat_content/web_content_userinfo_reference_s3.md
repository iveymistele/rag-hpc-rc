<div class="bd-callout bd-callout-warning">
<h4>S3 - Simple Storage Service</h4>
<p>S3 is a cloud-based object storage service. It has no size or file type restrictions, 
meaning it is ideal for backups, media files, and remote storage of original data.</p>

<p>Files stored in S3 are automatically private, geographically distributed redundantly,
and are 99.99999999999% resilient (13x9's).</p>
</div>


# S3 using the AWS CLI (Shell)

To install the AWS CLI for Linux or Windows, refer to this [documentation](https://rc.virginia.edu/userinfo/reference/aws-cli/).

List your buckets

    aws s3 ls

Make a bucket

    aws mb s3://my-bucket

List the contents of a bucket

    aws ls s3://my-bucket/                     # Displays the base contents of a bucket
    aws ls s3://my-bucket/and-folder/          # Displays the contents of a subdir
    aws ls s3://my-bucket/and-folder/*.png     # Displays all PNG files in the subdir

Copy an object into S3

    aws s3 cp my-local-file.zip s3://my-bucket/          # Copies a file into a bucket
    aws s3 cp my-local-file.zip s3://my-bucket/subdir/   # Copies a file into a subdir of a bucket
    aws s3 cp s3://my-bucket/file.zip ./                 # Copies a file from a bucket

Remove a file from S3

    aws s3 rm s3://my-bucket/subdir/my-file.zip   # Removes the file (called a 'key') from S3

Synchronize a local folder with S3

    aws s3 sync myfolder s3://my-bucket/myfolder/   # Syncs local folder's contents up to S3
    aws s3 sync s3://my-bucket/myfolder/ myfolder   # Syncs remote S3 folder down to local folder

- - -

# S3 using Python `boto3`

Moving objects in and out of S3 using `boto3` is similar in concept to the `awscli` but not identical. Below are two examples, one for copying a local file
into a bucket, and one for copying a file in S3 to the local computer.

<b>Upload files</b>
{{< gist nmagee c2be9caa4479bb11bb1b6097d7269946 >}}

<b>Download files</b>
{{< gist nmagee a8b42a126235a0366f7472efd4965d18 >}}

- - -

# S3 Desktop Tools

There are many other tools available for managing files in S3 that are command-line driven, web-based, or standalone applications. 

**Linux/MacOSX** users might be interested in `s3cmd` (command-line), Transmit, or Cyberduck (applications).

**Windows** users should explore CloudBerry, Cyberduck (applications), and `S3Express` (command-line).

- - -

# S3 Permissions / Access


To begin with, any S3 bucket that you create (and all files/objects in it) will be completely private to you, the account holder, until you make it otherwise.

If you need to share your files, you have multiple methods of controlling access to objects within your S3 bucket. The three methods are:

1. ACLs
2. S3 Bucket Policies
3. Presigned URLs


## ACLs


ACLs are the broadest and bluntest method of securing your buckets and their contents. They are less flexible for setting specific folder and file permissions.

* `private`
* `public-read`
* `public-read-write`
* `authenticated-read`
* `aws-exec-read`
* `bucket-owner-read`
* `bucket-owner-full-control`


## S3 Bucket Policies


S3 bucket policies grant various AWS accounts unique permissions to your bucket and objects within it. For instance, you may want to
grant a backup administrator the ability to WRITE new files to a bucket, but -- perhaps for auditing reasons -- you do not want her to have the ability
to DELETE files. This would be accomplished with an S3 bucket policy.

Here is a sample S3 bucket policy that grants read (GET) and write (PUT) access to the root user of another account (identified by the account number "111122223333"), 
but disallows all other actions.

    {
      "Version":"2012-10-17",
      "Statement":[
        {
          "Sid":"AddCannedAcl",
          "Effect":"Allow",
          "Principal": {"AWS": ["arn:aws:iam::111122223333:root"]},
          "Action":["s3:GetObject","s3:PutObject"],
          "Resource":["arn:aws:s3:::my-bucket/*"],
        }
      ]
    }

While their structure is similar, there is a difference between S3 bucket policies and IAM user policies. More about S3 bucket policies can be found [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).


## Presigned URLs


Presigned URLs are a method of creating a unique, expiring signed URL for a user to retrieve an object in S3 for a specific period of time. Here is an example of
how to create a presigned URL using the `awscli` that expires in 3600 seconds:

    aws s3 presign --expires-in 3600 s3://my-bucket-resources/my-file.zip

The output URL would look something like this:

    https://my-bucket-resources.s3.amazonaws.com/my-file.zip?
        \ AWSAccessKeyId=AKIAJH5Z6ORWK3XD6YYQ&Expires=1487978024
        \ &Signature=%2BKtyJlbZ4nxw2xhN7On52KTYGjI%3D


- - -


# S3 Lifecycle Management


Since it is technically "object storage" and not true "disk storage", S3 comes with the ability to automatically manage file, folder, or bucket lifecycles.
If, for instance, you had a bucket dedicated to storing your backups and you only wanted to keep 3 months' worth, this would be possible by creating a simple
lifecycle policy for your bucket that deletes files after that period of time.

Alternatively, you can create tiered lifecycle policies that will move your S3 data to Amazon's archival storage service named [Glacier](https://aws.amazon.com/glacier/) for a period of time, and then delete them after another period has passed.

To work with your bucket's lifecycle policies, use the AWS console and go to the properties for your bucket within the S3 service.


- - -


# S3 Pricing


Current pricing is [available here](https://aws.amazon.com/s3/pricing/), but generally S3 storage costs $0.023 per GB per month. However, be careful when 
moving very large sets of data as other costs may be incurred:

* All data transfer IN to S3 is free.
* Data transfer OUT to other AWS services is free.
* Data transfer OUT to the Internet (i.e. the UVA campus) costs nothing for the first GB each month, but $0.09 per GB beyond that.

<b>Sample storage costs (approximate, no data transfer costs included):</b>

<table class="table table-striped" style="width:50%;border:solid 1px #ccc;">
  <thead>
    <tr>
      <th>Size</th>
      <th style="text-align:right;">Monthly</th>
      <th style="text-align:right;">Annually</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10GB</td>
      <td align=right>$0.23</td>
      <td align=right>$2.76</td>
    </tr>
    <tr>
      <td>100GB</td>
      <td align=right>$2.30</td>
      <td align=right>$27.60</td>
    </tr>
    <tr>
      <td>1TB</td>
      <td align=right>$23.00</td>
      <td align=right>$276.00</td>
    </tr>
    <tr>
      <td>10TB</td>
      <td align=right>$230.00</td>
      <td align=right>$2,760.00</td>
    </tr>
  </tbody>
</table>


- - -


# Real-world Example


Below is a `bash` script that backs up a specific MySQL database, compresses it, names it with the date, then ships off to S3.

{{< gist nmagee caa3a3395682e1aeb39033201b096e23 >}}

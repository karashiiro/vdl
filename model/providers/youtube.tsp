import "@typespec/http";

using TypeSpec.Http;

@route("/providers/youtube")
namespace Vdl.Providers.YouTube;

model DownloadRequest {
    video: string;
}

model DownloadResponse {
    @header contentType: "application/octet-stream";
    @body video: bytes;
}

@post
op download(@body options: DownloadRequest): DownloadResponse;
